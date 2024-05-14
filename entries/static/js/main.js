document.addEventListener('DOMContentLoaded', function() {
    let displayObj = document.querySelectorAll('.entry_pnl');
    
    displayObj.forEach(function(el) {
        // Parse the inner text of the '.entry_pnl' element to get the numerical value
        let pnlValue = parseFloat(el.innerText);
        
        if(pnlValue < 0) {
            el.style.color = 'red';
        } else {
            el.style.color = 'green';
        }
    });
});