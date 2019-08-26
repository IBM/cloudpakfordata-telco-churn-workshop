# Cloud Pak for Data Workshop

## Workshop Table of Contents:

1. [Getting Started](./01-GettingStarted.md)
2. [Setting up the Server](./02-ServerSetUp.md)
3. **[Setting up the Dashboard](./03-DashboardSetUp.md)**

# Dashboard Set Up

Switch to your macOS client project, and open the `DisasterSocketClientDashboard.swift` file in Xcode. Add the following code to this file:

```swift
import Starscream

protocol DisasterSocketClientDashboardDelegate: class {
    func statusReported(client: DisasterSocketClientDashboard, person: Person)
    func clientConnected(client: DisasterSocketClientDashboard)
    func clientDisconnected(client: DisasterSocketClientDashboard)
    func clientErrorOccurred(client: DisasterSocketClientDashboard, error: Error)
    func clientReceivedToken(client: DisasterSocketClientDashboard, token: RegistrationToken)
}

enum DisasterSocketError: Error {
    case badConnection
}

class DisasterSocketClientDashboard {

}
```
***Starscream is a WebSocket library for iOS and  macOS, we use it so that the clients can connect to the server.***

This stubs out what you need to set up a WebSocket client in your macOS app. This might look familiar when you start working with your iOS client, but you will notice a couple of key differences.

At the very bottom of this file, outside of the scope of your `DisasterSocketClientDashboard` scope, add the following extension:

```swift
extension DisasterSocketClientDashboard: WebSocketDelegate {
    func websocketDidConnect(socket: WebSocketClient) {
        delegate?.clientConnected(client: self)
    }

    func websocketDidDisconnect(socket: WebSocketClient, error: Error?) {
        delegate?.clientDisconnected(client: self)
    }

    func websocketDidReceiveMessage(socket: WebSocketClient, text: String) {
        print("websocket message received: \(text)")
    }

    func websocketDidReceiveData(socket: WebSocketClient, data: Data) {
        print("websocket message received: \(String(describing: String(data: data, encoding: .utf8)))")
    }

    private func parse(_ data: Data) {

    }
}
```

You'll add more to this in just a moment, but first let's set up your initializer - add the following code at the top of your `DisasterSocketClientDashboard` class:

```swift
weak var delegate: DisasterSocketClientDashboardDelegate?
var address: String
var id: String?
public var disasterSocket: WebSocket?

init(address: String) {
    self.address = address
}
```

Next, add the following function to establish a connection:

```swift
public func attemptConnection() {
    guard let url = URL(string: "ws://\(self.address)/disaster") else {
        delegate?.clientErrorOccurred(client: self, error: DisasterSocketError.badConnection)
        return
    }
    let socket = WebSocket(url: url)
    socket.delegate = self
    disasterSocket = socket
    disasterSocket?.connect()
}
```

**Note:** it is very important to maintain a stored property of your WebSocket connection - if you don't save the memory of this connection outside of this function scope, you will try to work with something that is nil. Let's also add a way to disconnect your client:

```swift
public func disconnect() {
    disasterSocket?.disconnect()
}
```

Lastly, go to `ViewController.swift`, and inside the top of your `ViewController` definition, update your code to look like so:

```swift
class ViewController: NSViewController {
    var disasterClient = DisasterSocketClientDashboard(address: "localhost:8080")
    var annotationProcessingQueue = DispatchQueue(label: "com.ibm.annotationProcessingQueue")
    @IBOutlet weak var mapView: MKMapView?
    var annotations = [PersonAnnotation]()

    override func viewDidAppear() {
        super.viewDidAppear()
        disasterClient.delegate = self
        mapView?.delegate = self
    }
}
```

You'll need to make sure this controller conforms to your `DisasterSocketClientDashboardDelegate`. At the bottom of this file, add the following extension:

```swift
extension ViewController: DisasterSocketClientDashboardDelegate {
    func statusReported(client: DisasterSocketClientDashboard, person: Person) {

    }

    func removeDuplicateAnnotations(for person: Person) {

    }

    func clientConnected(client: DisasterSocketClientDashboard) {
        guard let currentLocation = mapView?.userLocation.coordinate else {
            return
        }
        let region = MKCoordinateRegion(center: currentLocation, latitudinalMeters: 1000, longitudinalMeters: 1000)
        self.mapView?.setRegion(region, animated: true)
    }

    func clientDisconnected(client: DisasterSocketClientDashboard) {
        print("client disconnected")
    }

    func clientErrorOccurred(client: DisasterSocketClientDashboard, error: Error) {
        print("error occurred: \(error.localizedDescription)")
    }

    func clientReceivedToken(client: DisasterSocketClientDashboard, token: RegistrationToken) {

    }
}
```

Then scroll up to the `connectDashboard:` function that occurs whenever you click the "Connect" button:

```swift
disasterClient.attemptConnection()
```

Make sure your server is running. Build and run your macOS dashboard, and accept location tracking. Click the connect button, and look at your server - you should have triggered a breakpoint. Nice work! Skip past the breakpoint, and make sure that the mapview zooms in to the right region.

## Using WebSockets to authenticate connections


Open up your server, and open `MyWebSocketService.swift`. Scroll to your `connected:` function, and remember that you are using a model object to verify that the dashboard should hang onto an id. In a second, you're going to go back to your dashboard and add code to handle the receipt of this token, but first, also notice that, whenever you receive a payload of type `Data` over your connection, you have a function to check what type of object it can be decoded into, and you act accordingly. Now let's make sure that your dashboard responds appropriately when you receive a registration token from the server.

Open your dashboard and go back to `DisasterSocketClientDashboard.swift`. Scroll to your `websocketDidReceiveData` function and add this:

```swift
parse(data)
```

Next, go into your `parse:` function and add the following code:

```swift
if let token = try? JSONDecoder().decode(RegistrationToken.self, from: data) {
    print("received registration token: \(token.tokenID)")
    delegate?.clientReceivedToken(client: self, token: token)
}
```

Whenever you get a `Data` message sent over your connection, you then see if you can decode a `RegistrationToken` object from it. If so, pass it to your view controller. Scroll up to your `disconnect:` function and add the following function underneath it:

```swift
public func confirm(_ dashboard: Dashboard) {
    self.id = dashboard.dashboardID
    do {
        disasterSocket?.write(data: try JSONEncoder().encode(dashboard))
    } catch let error {
        print("error writing dashboard registration to socket: \(error.localizedDescription)")
    }
}
```

Now, open `ViewController.swift`, so you can write code to take advantage of this function. Go inside your extension for your `DisasterSocketClientDashboardDelegate` and add the following code to your `clientReceivedToken` function:

```swift
guard let currentLocation = mapView?.userLocation.coordinate else {
    return
}
let dashboard = Dashboard(coordinate: Coordinate(latitude: currentLocation.latitude, longitude: currentLocation.longitude), dashboardID: token.tokenID)
client.confirm(dashboard)
```

If you want, add some breakpoints to the functions you have been working with so far. Restart both your server and your dashboard, and click the "Connect" button on your dashboard. In order:

1. Your dashboard tries to connect with the server
2. Your server gets the connection, and sends back a registration token
3. Your dashboard receives the token, and responds on the same connection with a confirmation
4. Your server receives the confirmation, and keeps track of which connection is the dashboard.

Now that you've set up your dashboard to work with your server, it's time to set up your iOS client.


# Next Steps

Continue to the [next page](./04-iOSSetUp.md) to set up the iOS Client.
