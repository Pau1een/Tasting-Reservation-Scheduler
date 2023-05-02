'use strict';


function removeSavedReservation(reservation_id) {
    const removed_reservation = {
    reservation_id: reservation_id,
    
    }
    
    fetch('/remove_saved_reservation', {
    method: 'POST',
    body: JSON.stringify(removed_reservation),
    headers: {'Content-Type': 'application/json'
    },
    })
    .then((response) => response.json())
    .then((data) => {
    if (data.success) {
        alert('Sucessfully removed reservation');  
    } 
    
    })
}

