# EOG iOS Swift Workshop

There are two major things that every iOS engineer works with on a regular basis. Our workshop today will walk you through the creation and handling of those things:

- Views
  - You have to display things to your users somehow, for frontend environments (like iOS) views are how that is done.
  - We will be using SwiftUI which is a library Apple introduced in 2019.
- Data
  - The data that drives a mobile app isn't always stored on the device itself, so what we're going to do is use an API to download data in JSON format.
  - We will create a model which the JSON data will be used to create so we can use this data within our views.

In our example application today we are going to create an application which lists out SpaceX launches and allows the user to tap into one and see more details.

## What am I doing?

There are 2 folders, `initial` and `final`. 

We're going to start in the `initial` folder which is a skeleton of the iOS Application we are going to make today. I have left some comments within it inside of placeholder files.

The `final` folder is what we're going to work towards and it is there for you if you just want to listen and not follow along, or if you just want to be able to reference back to what the completed product looks like.

We need a UI where we will eventually display the list of launches and allow the user to tap into some additional details.

### Let's go over some of the basic things we are going to do

We can use `ListView` which is provided to us by SwiftUI. Initially we can just make some placeholder code, something that looks like this

```swift
ListView {
    Text("First Item")
    Text("Second Item")
    Text("Third Item")
}
```

This code will get you a simple list view, but that's boring we want to pass data to our `ListView` so it can dynamically show elements. So let's create a simple `struct` and use that to drive our view.

```swift
// Create a model which can hold data for us
struct Launch {
    let name: String
}

// Creating a some sample data for testing our view
let launches = [
    Launch(name: "First Launch"),
    Launch(name: "Second Launch"),
    Launch(name: "Third Launch")
]

// Pass our launches array to the ListView
// We are then given individual launches by the ListView
// We can then access inidividual variables within the model and present it in the view as we please. In this case we are displaying the name variable.
ListView(launches, id: \.self) { launch in
    Text(launch.name)
}
```

To get data into your iOS application you can use APIs to pull in JSON data. This data can then be decoded into your model which can then be used throughout your app.

So here's an example JSON:

```json
[
    {
        "id": 1,
        "name": "First Item"
    },
    {
        "id": 2,
        "name": "Second Item"
    },
    {
        "id": 3,
        "name": "Third Item"
    }
]
```

Assuming that there is an API `https://givemethedata.com/data` how do you make the API call, get the data, then turn it into an array of your model.

```swift
// First lets create a model based on what our JSON looks like
struct Item {
    let id: Int
    let name: String
}

// Create a URL object
if let url = URL(string: "https://givemethedata.com/data")!

// Call the API (load the URL) and access the data returned
let (data, _) = try await URLSession.shared.data(from: url)

// Now we have the data, we need to take that and use it to create our `Item` objects
let items = try JSONDecoder().decode([Item].self, from: data)

// Congrats you have downloaded JSON data, and turned it into an array of objects
```

-----

With the following code examples and the `final` project which houses a simple completed iOS app, good luck and I am excited to see what you can create :)

Feel free to stop by the EOG Resources booth or send a message in the discord if you have any additional questions.