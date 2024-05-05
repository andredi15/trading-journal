document.addEventListener('DOMContentLoaded', function(closePrice, openPrice){
    let sum = closePrice - openPrice;
    let displayObj = document.querySelectorAll('.entry_pnl');
    
    displayObj.forEach(function(displayObj) {
        if(sum < 0)
            displayObj.style.color = 'red'
        else
            displayObj.style.color = 'green'
    })
})

