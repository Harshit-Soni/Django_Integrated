const analyze_result = document.getElementById('analyze_result');
const container = document.getElementById('show_sentiment');

$(function () {


    $('#scrape').click(function () {
        $.ajax({
            url: 'sentAjax',
            type: 'get',
            data: {
                product_url: $('#url').val()
            },
            success: function (response) {
                $('#scrape').text(response.seconds)
            }
        })
    })


	function get_response() {
        // console.log('here');
        // $('#url').attr('disabled', 'disabled');

        container.style.display = "block";
        
        var value = $('#text').val();

        if (value == "good") {
            var message = "POSITIVE";
            var html_string = `<div id="result" style="background-color: #26a69a;">${message}</div>`;
            container.innerHTML = html_string;
            // console.log("data");
        }
        else {
            var message = "NEGATIVE";
            var html_string = `<div id="result" style="background-color: red;">${message}</div>`;
            container.innerHTML = html_string;
            // console.log("data");
        }
    }

	$('#analyze').click(function(){
		get_response();
    }); 
    
    $('#text').keypress(function (e) {
		var key = e.which;
		if(key == 13)  // the enter key code
        {
            $('#analyze').click();
        }
    }); 
    
    function scrape_response() {
        scrape_data.style.display = "block";

    }

    // $('#scrape').click(function(){
    //     // $('#text').attr('disabled', 'disabled');
        
    //     container.style.display = "block";
	// 	var html_string = `<div id="analyze_result">
    //                         <div id="title">
    //                         boAt Rugged v3 Extra Tough Unbreakable Braided Micro: Amazon.in: Computers & Accessories
    //                         </div>
    //                         <div class="row" id="scrape_data">
    //                         <div class="col s6" id="positive_review">
    //                             <div>Positive Reviews</div>
    //                             <div>Positive Reviews</div>
    //                             <div>Positive Reviews</div>
    //                             <div>Positive Reviews</div>
    //                             <div>Positive Reviews</div>
    //                             <div>Positive Reviews</div>
    //                             <div>Positive Reviews</div>
    //                             <div>Positive Reviews</div>
    //                             <div>Positive Reviews</div>
    //                             <div>Positive Reviews</div>
    //                         </div>      
    //                         <div class="col s6 right" id="negative_review">
    //                             <div>Negative Reviews</div>
    //                             <div>Negative Reviews</div>
    //                             <div>Negative Reviews</div>
    //                             <div>Negative Reviews</div>
    //                             <div>Negative Reviews</div>
    //                             <div>Negative Reviews</div>
    //                             <div>Negative Reviews</div>
    //                             <div>Negative Reviews</div>
    //                             <div>Negative Reviews</div>
    //                             <div>Negative Reviews</div>
    //                         </div>
    //                         </div>
    //                         <div id="customer_sat">
    //                         Customer Satisfaction via Reviews is 25%
    //                         </div>
    //                     </div>`
    //     container.innerHTML = html_string;
    // }); 
    
    $('#url').keypress(function (e) {
		var key = e.which;
		if(key == 13)  // the enter key code
        {
            $('#scrape').click();
        }
    }); 
    
});


