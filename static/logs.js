// DocumentReady
$(function() {
    // if about undefined
    if ($.urlParam('about') == 0)
        $('#aboutbox').hide();

    //// ajax
    // fetching logfiles list
    $.getJSON("/logslist")
    .done(function(result) {
        // iterating through results
        $.each(result, function(i, field) {
            // populating tags
            $("#logslist").append('<li>' + field + ' (<a href="/log/' + field + '">download</a>)</li>');
        });
    })
    .fail(function(jqxhr, textStatus, error) {
        var err = textStatus + ", " + error;
        console.log("Request Failed: " + err);
    });
});