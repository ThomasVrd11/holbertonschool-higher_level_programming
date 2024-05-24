document.addEventListener("DOMContentLoaded", function() {
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
    const helloDiv = document.querySelector('#hello');

    fetch(url)
      .then(response => response.json())
      .then(data => {
        helloDiv.textContent = data.hello;
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  });
