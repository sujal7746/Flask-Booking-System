document.addEventListener("DOMContentLoaded", function () {
    const picker = document.getElementById("datetime-picker");
    
    // Optional: Set minimum date to today
    const today = new Date().toISOString().slice(0, 16);
    picker.setAttribute("min", today);
    
    // Optional: Add custom validation or styling
    picker.addEventListener("change", function () {
        const selectedDate = new Date(this.value);
        if (selectedDate < new Date()) {
            alert("Please select a future date and time!");
            this.value = today;
        }
    });
});