const generateGif = document.querySelector('button');
const output = document.querySelector('#output');

function fetchGif() {
  // TODO: replace the next line with your API key
  const apiKey = 'GgFZf48OO1lfS1C4hm9gMI0jt2sMIaFS';
  fetch(`http://api.giphy.com/v1/gifs/search?api_key=${apiKey}&q=hello&limit=1`)
    .then(data => {
      return data.json();
    })
    .then(json => {
      // display the json in the console for inspection
      console.log(json);
      // TODO: call the processJsonResponse function, passing along the data
      
    });
}

// TODO: complete the function below
function processJsonResponse(jsonData) {
  // TODO: parse the data and grab the "downsized url" from the images object
  
  // TODO: create an HTML string representing an img tag linking to the url above
  
  // TODO: append the HTML string to the end of the #output div tag.
  
}

/*
Challenges:
- modify the API call to instead search for a random gif
- modify the API call to select 10 gifs at a time, then have the 
  processJsonResponse function choose one at random
- add an <input> tag and allow the user to choose the query for searching.
*/
generateGif.addEventListener('click', fetchGif);