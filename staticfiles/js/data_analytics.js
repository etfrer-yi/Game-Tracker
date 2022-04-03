$("#form").submit(function(e) {
    e.preventDefault(); // avoid to execute the actual submit of the form.
    const form = $(this);
    const actionUrl = form.attr('action');
    const checkboxGroups = document.getElementsByClassName("checkbox");
    for (let i = 0; i < checkboxGroups.length; i++) {
        const checkboxes = checkboxGroups[i].children;
        let hasAtLeastOneCheckedCheckbox = false;
        let j = 0;
        for (j; j < checkboxes.length; ++j) {
            if (checkboxes[j].nodeName != "SPAN" && checkboxes[j].children[0].checked) {
                hasAtLeastOneCheckedCheckbox = true;
            }
        }
        if (!hasAtLeastOneCheckedCheckbox) {
            if (i == 0) {alert("You need to select at least one Battlefield game!")}
            if (i == 1) {alert("You need to select at least one platform!")}
            return;
        }
    }
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