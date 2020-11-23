$(function () {
    $('#go').click(function () {
        $.ajax({
            type: "get",
            url: "sentAjax",
            data: {
                product_url: $('#text').val()
            },
            success: function (response) {
                if (response.empty == true) {
                    alert('Enter Valid Amazon URL')
                    location.reload()
                }
                else {
                    $('#show_sentiment').css('display', 'block')
                    var html_string = `<div id="analyze_result">
                                    <div id="title">
                                    Title : ${response.title}
                                    </div>
                            
                                    <div id="title">
                                    Reviews Analyzed: ${response.len}
                                    </div>
                                    
                                    <div class="row" id="scrape_data">
                                    <div class="col" id="positive_review" style="text-align: center;">`
                    ans = '\n'
                    for (let index = 0; index < response.list.length; index++) {
                        ans += `<div>${response.list[index]}</div>\n`
                    }
                    html_string += ans
                    rest_string = `</div>      
                             </div>
                            
                             <div id="title">
                             Total Positive Reviews: ${response.posR} :: Total Negative Reviews: ${response.negR}
                             </div>
                         </div>`
                    html_string += rest_string
                    $('#show_sentiment').html(html_string);
                }
            }
        });
    });
    $('#text').keypress(function (e) {
        var key = e.which;
        if(key == 13)  // the enter key code
        {
            $('#go').click();
        }
    }); 
});

