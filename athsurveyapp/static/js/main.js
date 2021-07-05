$(document).ready(function(){
    // Bootsrap select picker
    $('select').selectpicker();

    // onchange employees base on company
    $('#branch').on('change', function(event) {
        var comp_id = event.target.value;
        var staffSelection =  $('#staff');

        console.log(comp_id);
        staffSelection.selectpicker('refresh');
        
        populateStaffSelection(comp_id).then(employees => {
            staffSelection.selectpicker('refresh');     
            options = ""
            for (var i=0; i<employees.length; i++){
                    options += `<option value="${employees[i].id}">${employees[i].name}</option>`;
            }
        

            staffSelection.empty().append(options);
            staffSelection.selectpicker('refresh');
            console.log(employees);
        });

        // $.ajax({
        //     type: "GET",
        //     url: `/employees/${comp_id}`,
        //     contentType: "application/json",
        //     dataType: "json",
        //     success: function(data) {
        //         options = ""
        //         for (var i=0; i<data.length; i++){
        //              options += `<option value="${data[i].id}">${data[i].name}</option>`;
        //         }
        //         staffSelection.selectpicker('refresh');
        //         staffSelection.empty().append(options);                
        //     },
        //     error: function(error) {
        //         console.log(error);
        //     }
        //   });


    })
});

async function populateStaffSelection(comp_id) {
    const response = await fetch(`/employees/${comp_id}`);
    const data = await response.json();
    return data;
}
