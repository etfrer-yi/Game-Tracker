$("#form").submit(function(e) {
    e.preventDefault(); // avoid to execute the actual submit of the form.
    const form = $(this);
    const actionUrl = form.attr('action');
    $.ajax({
        type: "GET",
        url: actionUrl,
        data: form.serialize(), // serializes the form's elements.
        success: function(plot) {
            const toBeReplacedByGraph = document.body.children[2];
            toBeReplacedByGraph.id = "replacement-graph";
            $("#replacement-graph").replaceWith(plot);
        }
    });

});