// Create a map object
var myMap = L.map("map", {
  center: [44.265477, -115.241797],
  zoom: 4
});

L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.satellite",
  accessToken: API_KEY
}).addTo(myMap);


// Define a markerSize function that will give each company a different radius based on its employee number
function markerSize(employeeNumber) {
  return employeeNumber / 3;
}

// Each company object contains the company's name, location and number of employee
var companies = [
  {
    name: "Amazon.com, Inc",
    location: [47.616858, -122.312920],
    employeeNumber: 840400
  },
  {
    name: "Apple Inc.",
    location: [37.335312, -122.007458],
    employeeNumber: 137000
  },
  {
    name: "Facebook, Inc.",
    location: [37.478686, -122.159222],
    employeeNumber: 44942
  },
  {
    name: "Google LLC",
    location: [37.422279, -122.084004],
    employeeNumber: 114096
  },
  {
    name: "Microsoft Corporation",
    location: [47.642964, -122.136755],
    employeeNumber: 151163
  }
];

// Loop through the cities array and create one marker for each city object
for (var i = 0; i < companies.length; i++) {
  L.circle(companies[i].location, {
    fillOpacity: 0.75,
    color: "white",
    fillColor: "grey",
    // Setting our circle's radius equal to the output of our markerSize function
    // This will make our marker's size proportionate to its population
    radius: markerSize(companies[i].employeeNumber)
  }).bindPopup("<h5>" + companies[i].name + "</h5> <hr> <h6>Employee Number: " + companies[i].employeeNumber + "</h6>").addTo(myMap);
}
  