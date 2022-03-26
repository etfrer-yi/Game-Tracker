const url = window.location.href;

$(document).ready(function () {
    let height1 = $('.content').height();
    let height2 = $('body').height();
    if (height1 > height2) {
        $('.sidebar').height(height1);
    } else {
        $('.sidebar').height(height2);
    }
    addRowHandlers();
});

function addRowHandlers() {
  let table = document.getElementsByClassName("table")[0];
  let rows = table.getElementsByTagName("tr");
  for (i = 0; i < rows.length; i++) {
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