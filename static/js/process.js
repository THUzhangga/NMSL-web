$('form').on('submit', function(event) {
       $.ajax({
          data : {
             text : $('#t').val(),
                 },
             type : 'POST',
             url : '/process'
            })
        .done(function(data) {
          $('#output').text(data.output).show();
      });
      event.preventDefault();
      });