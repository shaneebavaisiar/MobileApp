console.log('hello world')
var count = 0;
function cart() {
    count++;
    alert(count)
    document.getElementById('cart_counter').innerHTML = count;
    
}