$(function () {
	function get_response() {
		console.log('here')
		
		var value = $('#text_area').val();

		if (value.length > 0) {
			$('#text_area').val('');

			var html_string = `<div class="chatarea-inner user">${value}</div>`;

			$('.chatarea-outer').append(html_string);
			console.log(html_string)
			console.log($('.chatarea-outer'))

			var socket = new WebSocket('ws://127.0.0.1:8765');

			socket.onmessage = function(event) {
				data = JSON.parse(event.data);

				var html_string = `<div class="chatarea-inner chatbot">${data['response']}</div>`;
			
				$('.chatarea-outer').append(html_string);
				$('#text_area').val('');
			};

			var data = {'text': value};

			socket.onopen = function(event) {
				socket.send(JSON.stringify(data));
			};
		} else {
			// $('.no-message').removeClass('hidden');
			$('#text_area').val('');
		}
		console.log('completed')
	}

	$('#send').click(function(){
		console.log("send");
		get_response();
	});

	$('#text_area').keypress(function (e) {
		var key = e.which;
		if(key == 13)  // the enter key code
			{
			$('#send').click();
			$('#text_area').val('');
			}
	});

	function getmic_response(value) {
		console.log('here')

		if (value.length > 0) {

			var html_string = `<div class="chatarea-inner user">${value}</div>`;

			$('.chatarea-outer').append(html_string);
			console.log(html_string)
			console.log($('.chatarea-outer'))

			var socket = new WebSocket('ws://127.0.0.1:8765');

			socket.onmessage = function(event) {
				data = JSON.parse(event.data);

				var html_string = `<div class="chatarea-inner chatbot">${data['response']}</div>`;
			
				$('.chatarea-outer').append(html_string);
				$('#text_area').val('');
			};

			var data = {'text': value};

			socket.onopen = function(event) {
				socket.send(JSON.stringify(data));
			};
		} else {
			// $('.no-message').removeClass('hidden');
			$('#text_area').val('');
		}
		console.log('completed')
	}
	
	$("#mic").click(function(){
		const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
		const recognition = new SpeechRecognition();
		
		recognition.start();
		console.log("Activated");

		recognition.onresult = function(e){
			console.log("hi")
			let resultindex = e.resultIndex;
			let transcript = e.results[resultindex][0].transcript;
			getmic_response(transcript);
		// chatbotvoice(transcript);
		}
	  });
});