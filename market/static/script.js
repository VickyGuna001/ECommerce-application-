function removeFlash() {
    const element = document.getElementById("div_flash");
    element.remove();
}

//Market page cart

function checkPasswordStrength(password) {
    if (password.length >= 8 && /[0-9]/.test(password) && /[a-z]/.test(password)  ) {
        if (/[^\w]/.test(password)) {
            return "Strong Password";
        }
        return "Moderate Password";
    }
    else if (password.length == 0){
        return "null Password";
    }
    else {
        return "Weak Password";
    }
}
document.addEventListener("DOMContentLoaded", function () {
    let bucket = document.querySelector('.container');
    document.addEventListener("keyup",function(e){
      
        let password = document.querySelector('#password1').value;
        let strength = checkPasswordStrength(password);
        if (strength === "Weak Password") {
          bucket.classList.add('weak');
          bucket.classList.remove('moderate');
          bucket.classList.remove('strong');
        } else if (strength === "Strong Password") {
          bucket.classList.remove('weak');
          bucket.classList.remove('moderate');
          bucket.classList.add('strong');
        } else if (strength === 'null Password') {
            bucket.classList.remove('weak');
          bucket.classList.remove('moderate');
          bucket.classList.remove('strong');
        }
        else {
          bucket.classList.remove('weak');
          bucket.classList.add('moderate');
          bucket.classList.remove('strong');
        
      }
    }) })

    //Market page cart

    const cart = [];
    let total = 0;
  
    // Function to add an item to the cart
    function addToCart(id, productName, price) {
      price = parseInt(price);
  
      // Check if the item is already in the cart
      const existingItemIndex = cart.findIndex(item => item.id === id);
  
      if (existingItemIndex !== -1) {
        // If the item is already in the cart, increment its quantity
        cart[existingItemIndex].qty += 1;
        cart[existingItemIndex].price += price;
      } else {
        // If the item is not in the cart, add it as a new item
        cart.push({id, productName, price, qty: 1 });
      }
  
      total += price;
      updateCartDisplay();
    }
  
    // Function to remove an item from the cart
    // Function to remove an item from the cart
  function removeFromCart(index) {
    const removedItem = cart.splice(index, 1)[0];
    total -= removedItem.price;
    updateCartDisplay();
  }
  
  
    // Function to update the cart display
    function updateCartDisplay() {
      const cartItems = document.getElementById('cart-items');
      const cartTotal = document.getElementById('cart-total');
      var qty = 0;
  
      cartItems.innerHTML = '';
      cart.forEach((item, index) => {
        const listItem = document.createElement('li');
        listItem.innerHTML = ` <div class='items-list'>
            ${item.productName} <br> <div class="qty">${"&#8377"} ${item.price} <br> Qty: ${item.qty}</div>
            <button class='chk-btn' onclick="removeFromCart(${index})">Remove</button>
            </div><hr>
          `;
        cartItems.appendChild(listItem);
      });
  
      cartTotal.textContent = total;
    }

    // Get all elements with the class "stars"
const stars = document.querySelectorAll('.stars');

// Loop through each element
stars.forEach(star => {
  // Get the rating value from the 'data-rating' attribute
  const rating = parseFloat(star.getAttribute('data-rating'));
  // Set the CSS variable '--rating' to the percentage value
  star.style.setProperty('--rating', (rating / 5) * 100 + '%');
});
