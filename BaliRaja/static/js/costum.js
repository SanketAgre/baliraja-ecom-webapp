$(document).ready(function() {    
    $('.increment-btn').click(function(e){
        e.preventDefault();
        var product_qty = $(this).closest('.product_data').find('.prod_qty').val();
        var inc_value=$(this).closest('.product_data').find('.qty-input').val();
        var value = parseInt(inc_value,10);
        value=isNaN(value) ? 0: value;
        if(value < 10)
        {
            value++;
            $(this).closest('.product_data').find('.qty-input').val(value);
        }

        if(product_qty < value){
            $('.prod_qty_err_msg').show();
        }
        else{
            $('.prod_qty_err_msg').hide();
        }
    });
});

$(document).ready(function() {
    $('.decrement-btn').click(function(e){
        e.preventDefault();
        var product_qty = $(this).closest('.product_data').find('.prod_qty').val();
        var dec_value=$(this).closest('.product_data').find('.qty-input').val();
        var value = parseInt(dec_value,10);
        value=isNaN(value) ? 0: value;
        if(value > 1)
        {
            value--;
            $(this).closest('.product_data').find('.qty-input').val(value);
        }

        if(product_qty < value){
            $('.prod_qty_err_msg').show();
        }
        else{
            $('.prod_qty_err_msg').hide();
        }
    });

    $('.addToCartBtn').click(function (e) {
        e.preventDefault();

        var Product_id = $(this).closest('.product_data').find('.prod_id').val();
        var product_qty = $(this).closest('.product_data').find('.qty-input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "/add-to-cart",
            data: {
                'Product_id':Product_id,
                'product_qty':product_qty,
                csrfmiddlewaretoken: token
            },
            success:function (response){
                console.log(response)
                alertify.success(response.status)
            },

        });
    });
    $('.addToWishlist').click(function (e) {
        e.preventDefault();

        var Product_id = $(this).closest('.product_data').find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        
        $.ajax({
            method: "POST",
            url: "/add-to-wishlist",
            data: {
                'Product_id':Product_id,
                csrfmiddlewaretoken: token
            },
            success:function (response){
                console.log(response)
                alertify.success(response.status)
            },

        });
    });

    $('.changeQuantity').click(function (e) {
        e.preventDefault();

        var Product_id = $(this).closest('.product_data').find('.prod_id').val();
        var product_qty = $(this).closest('.product_data').find('.qty-input').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        $.ajax({
            method: "POST",
            url: "/update-cart",
            data: {
                'Product_id':Product_id,
                'product_qty':product_qty,
                csrfmiddlewaretoken: token
            },
            success:function (response){
                console.log(response)
                alertify.success(response.status)
            },

        });
    });
    $(document).on('click', '.delete-cart-item', function(e){
        e.preventDefault();

        var Product_id = $(this).closest('.product_data').find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        
        $.ajax({
            method: "POST",
            url: "/delete-cart-item",
            data: {
                'Product_id':Product_id,
                csrfmiddlewaretoken: token
            },
            success:function (response){
                alertify.success(response.status)
                $('.cartdata').load(location.href + " .cartdata");
            },

        });
    });
    $(document).on('click', '.delete-wishlist-item', function(e){
        e.preventDefault();

        var Product_id = $(this).closest('.product_data').find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        
        $.ajax({
            method: "POST",
            url: "/delete-wishlist-item",
            data: {
                'Product_id':Product_id,
                csrfmiddlewaretoken: token
            },
            success:function (response){
                alertify.success(response.status)
                $('.wishdata').load(location.href + " .wishdata");
            },

        });
    });
    
    $(document).on('click', '.checkout-item', function(e){
        e.preventDefault();

        var Product_id = $(this).closest('.product_data').find('.prod_id').val();
        var token = $('input[name=csrfmiddlewaretoken]').val();
        
        $.ajax({
            method: "POST",
            url: "/checkoutitem",
            data: {
                'Product_id':Product_id,
                csrfmiddlewaretoken: token
            },
            success:function (response){
                console.log(response);
                alertify.success(response.status)
                location.href='products/checkout.html';
                // $('.cartdata').load(location.href + " .cartdata");
            },
            error:function(error){
                console.log(error);
            }
        });
    });
    
});