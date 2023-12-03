// search.js

document.addEventListener("DOMContentLoaded", function() {
    const searchInput = document.getElementById("search-input");
    const searchResults = document.getElementById("search-results");
  
    searchInput.addEventListener("input", function() {
      const searchValue = searchInput.value.trim();
  
      if (searchValue.length > 0) {
        searchResults.innerHTML = "Loading...";
  
        const xhr = new XMLHttpRequest();
        xhr.open("GET", `/search/?search=${searchValue}`, true);
        xhr.onreadystatechange = function() {
          if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
            const response = JSON.parse(xhr.responseText);
            displaySearchResults(response.results);
          } else if (xhr.readyState === XMLHttpRequest.DONE && xhr.status !== 200) {
            searchResults.innerHTML = "Error occurred.";
          }
        };
        xhr.send();
      } else {
        searchResults.innerHTML = "";
      }
    });
  
    function displaySearchResults(results) {
      if (results.length === 0) {
        searchResults.innerHTML = "No results found.";
        return;
      }
  
      let output = "";
      for (const result of results) {
        output += `<p>Name: ${result.name}</p>`;
        output += `<p>Mobile: ${result.mobile}</p>`;
        output += `<p>Occupation: ${result.occupation}</p>`;
        output += "<hr>";
      }
  
      searchResults.innerHTML = output;
    }
  });
  