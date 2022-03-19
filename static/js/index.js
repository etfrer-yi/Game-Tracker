const url = window.location.href;

$(document).ready(function () {
    let height1 = $('.content').height();
    let height2 = $('body').height();

    if (height1 > height2) {
        $('.sidebar').height(height1);
    } else {
        $('.sidebar').height(height2);
    }

    addRowHandlers()
});

function addRowHandlers() {
  var table = document.getElementsByClassName("table")[0];
  var rows = table.getElementsByTagName("tr");
  for (i = 0; i < rows.length; i++) {
    var currentRow = table.rows[i];
    var createClickHandler = function(row) {
        return function() {
            console.log("row:" + row);
        };
    }
    currentRow.onclick = createClickHandler(currentRow);
  }
}