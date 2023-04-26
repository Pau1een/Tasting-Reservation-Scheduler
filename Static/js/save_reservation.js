'use strict';

const saveReservationTime = (reservation_id) => {
    console.log("saving reservation")
    const selectedDate = document.getElementById("datepicker").value;
    const startTime = document.getElementById("start-time").value;
    const endTime = document.getElementById("end-time").value;
    const body = {
        selected_date: selectedDate,
        start_time: startTime,
        end_time: endTime,
        reservation_id: reservation_id
    }
    fetch('/save_reservation', {
        method: "POST",
        body: JSON.stringify(body),
        headers: {'Content-Type': 'application/json'
        },
    })
    .then((response) => response.text())
    .then((data) => swal("Saved!"))
}


function removeFromFavorite(recipe_link) {
    console.log(recipe_link)
    const removed_recipe = {
    recipe_link: recipe_link,
    }
    
    fetch('/remove_saved_recipe', {
    method: 'POST',
    body: JSON.stringify(removed_recipe),
    headers: {'Content-Type': 'application/json'
        },
    })
    .then((response) => response.json())
    .then((data) => {
    if (data.success) {
        // alert('Sucessfully removed recipe!');  
        swal("Sucessfully removed recipe!");
    } 
    })
}
