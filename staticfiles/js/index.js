const url = window.location.href;

$(document).ready(function () {
    addRowHandlers();
});

function addRowHandlers() {
  let table = document.getElementsByClassName("table")[0];
  let rows = table.getElementsByTagName("tr");
  for (i = 1; i < rows.length; i++) { // we start at 1 instead of 0 because we want to avoid the first row of table headers
    let currentRow = table.rows[i];
    let createClickHandler = function(row) {
        return function() {
            const rank = row.children[0].innerHTML;
            const urlWithoutPagination = url.split("?")[0]; // splits on the query params "?"
            window.location.replace(urlWithoutPagination + rank + "/");
        };
    }
    currentRow.onclick = createClickHandler(currentRow);
  }
}