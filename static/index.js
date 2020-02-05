// DocumentReady
$(function() {
    //// init
    $('.loadinggif').hide();

    // if about undefined
    if ($.urlParam('about') == 0)
        $('#aboutbox').hide();

    // predictbutton listener
    $("#predictbutton").click(function() {
        // reading form values
        var country = $("#country").val();
        var dateinput = $("#dateinput").val();
        // clearing and showing gifs
        $("#results").empty();
        $("#resultsgif").show();
        // ajax call
        $.getJSON("/predict?country=" + country + "&target_date=" + dateinput)
        .done(function(result) {
            // hiding gif
            $("#resultsgif").hide();
            if (result.length == 0) {
                $("#results").append('<p class="m-1">No response</p>');
            } else {
                // iterating through results
                $.each(result, function(i, field) {
                    // populating tags
                    $("#results").append('<p><b>' + i + "</b>: " + field + '</p>');
                });
            }
        })
        .fail($.ajaxError);
    });

    // modelbutton listener
    $("#modelbutton").click(function() {
        // reading form values
        var regressor = $("#regressor").val();
        // clearing and showing gifs
        $("#results").empty();
        $("#resultsgif").show();
        // ajax call
        $.getJSON("/train?regressor=" + regressor)
        .done(function(result) {
            // hiding gif
            $("#resultsgif").hide();
            $("#results").append('<p>Model training successful!</p>');
        })
        .fail($.ajaxError);
    });

});