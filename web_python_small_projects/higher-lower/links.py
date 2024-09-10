links = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Number Links</title>
    <style>
        .link-button, .home-button {
            text-decoration: none;
            font-size: 24px;
            color: #ffffff; /* Default text color */
            background-color: #007bff; /* Default background color */
            padding: 10px 20px;
            border-radius: 5px;
            transition: background-color 0.3s, color 0.3s;
            outline: none; /* Remove default focus outline */
            cursor: pointer; /* Indicate that it is clickable */
            margin: 5px;
        }
        .link-button:hover, .home-button:hover {
            background-color: #0056b3; /* Darker blue for hover effect */
        }
        .link-button.visited {
            background-color: #000000; /* Black background for visited */
            color: #ffffff; /* White text color for visited */
            cursor: default; /* Change cursor to indicate non-clickable */
        }
        .home-button {
            background-color: #28a745; /* Green background for home button */
        }
    </style>
</head>
<body>
    <div style="text-align: center;">
        <p style="font-size: 20px; font-weight: bold; margin-bottom: 20px;">Choose a number:</p>
        <div style="display: flex; justify-content: center; flex-wrap: wrap; gap: 10px;">
            <a href="/" class="home-button">Home</a>
            <a href="/0" class="link-button" data-number="0">0</a>
            <a href="/1" class="link-button" data-number="1">1</a>
            <a href="/2" class="link-button" data-number="2">2</a>
            <a href="/3" class="link-button" data-number="3">3</a>
            <a href="/4" class="link-button" data-number="4">4</a>
            <a href="/5" class="link-button" data-number="5">5</a>
            <a href="/6" class="link-button" data-number="6">6</a>
            <a href="/7" class="link-button" data-number="7">7</a>
            <a href="/8" class="link-button" data-number="8">8</a>
            <a href="/9" class="link-button" data-number="9">9</a>
        </div>
        <br>
        
    </div>

</body>
</html>

'''