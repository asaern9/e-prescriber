
function ReloadPrice() {
    let quantity = document.getElementById("quantity").value;
    let price = document.getElementById("price");
    let price2 = price.options[price.selectedIndex].value;
    let total = quantity * price2;
    document.getElementById("total_price").innerHTML = "Total price:GHC "+ total.toString();
}