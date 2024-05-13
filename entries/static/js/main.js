
document.addEventListener('DOMContentLoaded', function(){
        let displayObj = document.querySelectorAll('.entry_pnl');
        
        displayObj.forEach(function(el) {
            let pnlValue = parseInt(el.innerText)
            if(pnlValue < 0) {
                el.style.color = 'red'
            } else {
                el.style.color = 'green'
            }
        })
    })
    