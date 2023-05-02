'use strict';

const date = document.querySelector("#datepicker");
const startTime = document.querySelector('#time');
const reservation = document.querySelector('#reservation');

reservation.addEventListener('submit', (evt) => {
    evt.preventDefault();
    const reservationDate = date.value; 
    const reservationStartTime = startTime.value;
    submitReservation(reservationDate, reservationStartTime);
});

function submitReservation(date, start_time) {
    const input = {
    date: date,
    start_time: start_time,
}

fetch('/book', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify(input)
})
.then((response) => response.json())
.then((data) => {
    if (data.success) {
    alert('Reservation added!');  
    } else {
    alert('Reservation already taken. Try again.');
    }
})

}
