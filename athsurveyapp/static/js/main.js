$(document).ready(function(){
    // Bootsrap select picker
    $('select').selectpicker();

    // onchange employees base on company
    $('#branch').on('change', function(event) {
        var comp_id = event.target.value;
        var staffSelection =  $('#staff');

        console.log(comp_id);    

        $.ajax({
            type: "GET",
            url: `/employees/${comp_id}`,
            contentType: "application/json",
            dataType: "json",
            success: function(data) {
                options = ""
                for (var i=0; i<data.length; i++){
                     options += `<option value="${data[i].id}">${data[i].name}</option>`;
                }
                staffSelection.empty().append(options);
                staffSelection.selectpicker('refresh');

            },
            error: function(error) {
                console.log(error);
            }
          });


    })
});

