const datePicker = document.getElementById('datepicker');
let startTime = document.getElementById('start-time');
let endTime = document.getElementById('end-time');

startTime.addEventListener('change', updateEndTime);
endTime.addEventListener('change', updateStartTime);

function updateEndTime() {
    let selectedStart = new Date(startTime.value);
    let minEndTime = new Date(selectedStart.getTime() + 30 * 60000);
    let maxEndTime = new Date(selectedStart.getTime() + 2 * 60 * 60000);
    let formattedMinEndTime = formatDate(minEndTime);
    let formattedMaxEndTime = formatDate(maxEndTime);
    endTime.setAttribute('min', formattedMinEndTime);
    endTime.setAttribute('max', formattedMaxEndTime);
    if (new Date(endTime.value) < minEndTime) {
        endTime.value = formattedMinEndTime;
}
}

function updateStartTime() {
    let selectedEnd = new Date(endTime.value);
    let maxStartTime = new Date(selectedEnd.getTime() - 30 * 60000);
    let formattedMaxStartTime = formatDate(maxStartTime);
    startTime.setAttribute('max', formattedMaxStartTime);
    if (new Date(startTime.value) > maxStartTime) {
        startTime.value = formattedMaxStartTime;
}
}

function formatDate(date) {
  let year = date.getFullYear();
  let month = date.getMonth() + 1;
  let day = date.getDate();
  let hour = date.getHours();
  let minute = date.getMinutes();
  let formattedDate = `${year}-${month.toString().padStart(2, '0')}-${day.toString().padStart(2, '0')}T${
