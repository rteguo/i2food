(function($){
	'use script';


	var $loader = $('#preloader');
    if($loader.length > 0){
		$(window).on('load', function(event) {
	        $('#preloader').delay(500).fadeOut(500);
		});
	}



	// Scroll Area
	var $scroll = $('.scroll-area');
	if($scroll.length > 0){
		$(document).ready(function(){
		    $('.scroll-area').click(function(){
		      	$('html').animate({
		        	'scrollTop' : 0,
		      	},700);
		      	return false;
		    });
		    $(window).on('scroll',function(){
		      	var a = $(window).scrollTop();
		      	if(a>400){
		            $('.scroll-area').slideDown(300);
		        }else{
		            $('.scroll-area').slideUp(200);
		        }
		    });
		});
	}

	//video
		var $video = $('.technology-video a');
	    if($video.length > 0){
			$('.technology-video a').magnificPopup({
			  	type: 'iframe',
			});	
	 }
		

	///add minicart login serach
	  let searchForm = document.querySelector('.search-form');

        document.querySelector('#search-btn').onclick = () =>{
         searchForm.classList.toggle('active');
         shoppingCart.classList.remove('active');
        }


		//Manage add to cart

		// Function to update the cart size
        function updateCartSize() {
            $.ajax({
                url: '/cart_size',
                method: 'GET',
                success: function(data) {
                    $('#cart-size').text(data.cart_size);
                }
            });
        }

        // Update the cart size initially
        updateCartSize();
		
		 // AJAX to add an item to the cart
		 document.querySelectorAll('.add-to-cart').forEach(function(button) {
			button.addEventListener('click', function() {
				const productId = button.getAttribute('data-id');
				const qty = document.getElementById("qty").value;

				fetch('/add_to_cart', {
					method: 'POST',
					body: new URLSearchParams({ 'product_id': productId, 'qty': qty }),
					headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
				})
				.then(response => response.json())
				.then(data => {
					alert(data.message);
					// Update the cart size after add item
					updateCartSize();
				})
				.catch(error => console.error('Error:', error));
			});

		});

		//Ajax to remove item in the cart
		document.querySelectorAll('.remove-from-cart').forEach(function(button) {
			button.addEventListener('click', function() {
				var productId = button.getAttribute('data-id');

				fetch('/remove_from_cart', {
					method: 'POST',
					body: new URLSearchParams({ 'product_id': productId }),
					headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
				})
				.then(response => response.json())
				.then(data => {
					alert(data.message);
					//Reload the cart page after successful remove
					location.reload();
				})
				.catch(error => console.error('Error:', error));
			});
		});

		// Ajax to submit order by customer
		document.querySelectorAll('.submit-order').forEach(function(button) {
			button.addEventListener('click', function() {
				var orderTotal = document.getElementById("order_total").value;

				fetch('/submit_order', {
					method: 'POST',
					body: new URLSearchParams({ 'order_total': orderTotal }),
					headers: { 'Content-Type': 'application/x-www-form-urlencoded' }
				})
				.then(response => response.json())
				.then(data => {
					alert(data.message);
					//Reload the cart page after successful remove
					window.location.href = '/shop';
				})
				.catch(error => console.error('Error:', error ));
			});
		});

		// Add new product
		$("#save-product").submit(function(event) {
			event.preventDefault();

			// Prepare form data for Ajax
			var formData = new FormData(this);

			// Send a POST request to the server
			$.ajax({
				type: 'POST',
				url: '/save_product',
				data: formData,
				contentType: false,
				processData: false,
				success: function(response) {
					// Set and display the message from server
					$("#message").html(response.message);
					//alert(response.message);

					//Reload the list of foods after successful added
					if (response.message == "Product added successfully"){
						window.location.href = '/adminproducts';
					}
					//
				},
				error: function(error) {
					$("#message").html("Error saving product.");
				}
			});
		});


		// Update product
		$("#update-product").submit(function(event) {
			event.preventDefault();

			// Prepare form data for Ajax
			var formData = new FormData(this);

			// Send a POST request to the server
			$.ajax({
				type: 'POST',
				url: '/update_product',
				data: formData,
				contentType: false,
				processData: false,
				success: function(response) {
					// Set and display the message from server
					$("#message").html(response.message);
					//alert(response.message);

					//Reload the list of foods after successful added
					if (response.message == "Product updated successfully"){
						window.location.href = '/adminproducts';
					}
					//
				},
				error: function(error) {
					$("#message").html("Error updating product.");
				}
			});
		});

		// User Login 
		$("#login-user").submit(function(event) {
			event.preventDefault();

			// Prepare form data for Ajax
			var formData = new FormData(this);

			// Send a POST request to the server
			$.ajax({
				type: 'POST',
				url: '/loginprocess',
				data: formData,
				contentType: false,
				processData: false,
				success: function(response) {
					// Set and display the message from server
					$("#message").html(response.message);
					//alert(response.message);

					//Reload the homepage after successful login
					if (response.message == "Login successfully."){
						window.location.href = '/';
					}
					//
				},
				error: function(error) {
					$("#message").html("Error user log in.");
				}
			});
		});

		// Create new user form
		$("#add-user").submit(function(event) {
			event.preventDefault();

			// Prepare form data for Ajax
			var formData = new FormData(this);

			// Send a POST request to the server
			$.ajax({
				type: 'POST',
				url: '/userprocess',
				data: formData,
				contentType: false,
				processData: false,
				success: function(response) {
					// Set and display the message from server
					$("#message").html(response.message);
					//alert(response.message);

					//Reload the homepage after successful login
					if (response.message == "User crate successfully."){
						window.location.href = '/adminusers';
					}
					//
				},
				error: function(error) {
					$("#message").html("Error user log in.");
				}
			});
		});

	
		
    //     window.onscroll = () =>{
    //     searchForm.classList.remove('active');
    //     shoppingCart.classList.remove('active');
    //     loginForm.classList.remove('active');
        
    // }


    // close
    // document.querySelector('#close-btn').onclick = () =>{
    //    shoppingCart.classList.remove('active');
    // }
    //  document.querySelector('#close-login').onclick = () =>{
    //    loginForm.classList.remove('active');
    // }



   		///banner
   		var $full = $('.hero-slider-full2');
		    if($full.length > 0){
		    $(document).ready(function(){
			  	$(".hero-slider-full2").owlCarousel({
			  		loop:true,
			  		center:true,
			  		items:1,
			  		autoplay: true,
			  		nav: true,
		  			navText: ["<i class='fas fa-angle-left'></i>","<i class='fas fa-angle-right'></i>"],
			  	});
			});
			}

		///product iteam slider
   		var $full = $('.item-single-slider');
		    if($full.length > 0){
		    $(document).ready(function(){
			  	$(".item-single-slider").owlCarousel({
			  		loop:false,
			  		items:1,
			  		autoplay: false,
			  		nav: true,
			  		margin:15,
			  		nav:false,
			  	});
			});
			}

			///product deal
   		var $bounus = $('.bounus-slider');
		    if($bounus.length > 0){
		    $(document).ready(function(){
			  	$(".bounus-slider").owlCarousel({
			  		loop: true,
		            autoplay: true,
		            autoplayTimeout: 9000,
		            items: 2,
			  		margin:10,
			  		nav:true,
			  		navText: ["<i class='fas fa-angle-left'></i>","<i class='fas fa-angle-right'></i>"],
			  		responsive:{
		  				0:{
		  					items:1,
		  				},
		  				430:{
		  					items:1,
		  				},
		  				767:{
		  					items:1,
		  				},
		  				991:{
		  					items:2,
		  				},
		  			}
			  	});
			});
			}

			//product
	    	var $product = $('.product-slider');
		    if($product.length > 0){
		      $(document).ready(function(){
			  	$(".product-slider").owlCarousel({
			  		loop:true,
			  		margin:10,
			  		items:4,
			  		autoplay: true,
			  		nav: true,
		  			navText: ["<i class='fas fa-angle-left'></i>","<i class='fas fa-angle-right'></i>"],
		  			responsive:{
		  				0:{
		  					items:1,
		  				},
		  				430:{
		  					items:2,
		  				},
		  				767:{
		  					items:3,
		  				},
		  				991:{
		  					items:4,
		  				},
		  			}
			  	});
			});
	  	}

	  	///category
	      var $category_slider= $('.category-slider');
	 		if($category_slider.length > 0){
		       $(document).ready(function(){
			  	$(".category-slider").owlCarousel({
			  		loop:true,
			  		margin:10,
			  		items:4,
			  		autoplay: false,
			  		nav: true,
		  			navText: ["<i class='fas fa-angle-left'></i>","<i class='fas fa-angle-right'></i>"],
		  			responsive:{
		  				0:{
		  					items:1,
		  				},
		  				430:{
		  					items:2,
		  				},
		  				767:{
		  					items:3,
		  				},
		  				991:{
		  					items:4,
		  				},
		  			}
			  	});
			});
	      } 

	      ///client
	    var $clint = $('.client-slider');
	    if($clint.length > 0){
		 $(document).ready(function(){
		    $(".client-slider").owlCarousel({ 
	            loop: true,
	            autoplay: true,
	            autoplayTimeout: 9000,
	            items: 2,
	            nav: true,
  			    navText: ["<i class='fas fa-angle-left'></i>","<i class='fas fa-angle-right'></i>"],
	            responsive : {
				    // breakpoint from 0 up
				    0 : {
				        items:1,
				    },
				    // breakpoint from 480 up
				    480 : {
				        items:1,
				    },
				    // breakpoint from 768 up
				    768 : {
				       items:1,
				    },
				      929 : {
				       items:2,
				    }
				}
		    });
		});
	}


	//blog
	var $news = $('#news-slider');
	 if($news.length > 0){
	$(document).ready(function() {
	    $("#news-slider").owlCarousel({
	        items : 3,
	        itemsDesktop:[1199,2],
	        itemsDesktopSmall:[980,2],
	        itemsTablet:[650,1],
	        pagination:false,
	        navigation:true,
	        nav: true,
		    navText: ["<i class='fas fa-angle-left'></i>","<i class='fas fa-angle-right'></i>"],
		    responsive : {
			    // breakpoint from 0 up
			      0:{
	  					items:1,
	  				},
	  				430:{
	  					items:1,
	  				},
	  				767:{
	  					items:2,
	  				},
	  				991:{
	  					items:3,
	  				},
				}
		    });
		});
	}	
	// slick

	
	//ui
	var $tab = $('#tabs');
	if($tab.length > 0){
	$( function() {
	    $( "#tabs" ).tabs();
	  } );
	}


		//===== Mobile Menu
    $('.mobile-menu-open').on('click', function(){
        $('.mobile-off-canvas-menu').addClass('open')
        $('.overlay').addClass('open')
    });
    

    $('.close-mobile-menu').on('click', function(){
        $('.mobile-off-canvas-menu').removeClass('open')
        $('.overlay').removeClass('open')
    });
    
    $('.overlay').on('click', function(){
        $('.mobile-off-canvas-menu').removeClass('open')
        $('.overlay').removeClass('open')
    });


    
    
   
    
    /*Variables*/
    var $offCanvasNav = $('.mobile-main-menu'),
        $offCanvasNavSubMenu = $offCanvasNav.find('.mega-sub-menu, .sub-menu, .submenu-item ');

    /*Add Toggle Button With Off Canvas Sub Menu*/
    $offCanvasNavSubMenu.parent().prepend('<span class="mobile-menu-expand"></span>');

    /*Close Off Canvas Sub Menu*/
    $offCanvasNavSubMenu.slideUp();

    /*Category Sub Menu Toggle*/
    $offCanvasNav.on('click', 'li a, li .mobile-menu-expand, li .menu-title', function(e) {
        var $this = $(this);
        if (($this.parent().attr('class').match(/\b(menu-item-has-children|has-children|has-sub-menu)\b/)) && ($this.attr('href') === '#' || $this.hasClass('mobile-menu-expand'))) {
            e.preventDefault();
            if ($this.siblings('ul:visible').length) {
                $this.parent('li').removeClass('active-expand');
                $this.siblings('ul').slideUp();
            } else {
                $this.parent('li').addClass('active-expand');
                $this.closest('li').siblings('li').find('ul:visible').slideUp();
                $this.closest('li').siblings('li').removeClass('active-expand');
                $this.siblings('ul').slideDown();
            }
        }
    });
	
	
	
class Slider {
  constructor (rangeElement, valueElement, options) {
    this.rangeElement = rangeElement
    this.valueElement = valueElement
    this.options = options

    // Attach a listener to "change" event
    this.rangeElement.addEventListener('input', this.updateSlider.bind(this))
  }

  // Initialize the slider
  init() {
    this.rangeElement.setAttribute('min', options.min)
    this.rangeElement.setAttribute('max', options.max)
    this.rangeElement.value = options.cur

    this.updateSlider()
  }

  // Format the money
  asMoney(value) {
    return '$' + parseFloat(value)
      .toLocaleString('en-US', { maximumFractionDigits: 2 })
  }

  generateBackground(rangeElement) {   
    if (this.rangeElement.value === this.options.min) {
      return
    }

    let percentage =  (this.rangeElement.value - this.options.min) / (this.options.max - this.options.min) * 100
    return 'background: linear-gradient(to right, #80B500, #93C794 ' + percentage + '%, #93C794 ' + percentage + '%, white 100%)'
  }

  updateSlider (newValue) {
    this.valueElement.innerHTML = this.asMoney(this.rangeElement.value)
    this.rangeElement.style = this.generateBackground(this.rangeElement.value)
  }
}

let rangeElement = document.querySelector('.range [type="range"]')
let valueElement = document.querySelector('.range .range__value span') 

let options = {
  min: 20,
  max: 200,
  cur: 375
}

if (rangeElement) {
  let slider = new Slider(rangeElement, valueElement, options)

  slider.init()
}

}(jQuery));
