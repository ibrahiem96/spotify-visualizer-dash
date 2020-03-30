// client-side js
// run by the browser each time your view template is loaded

$(function() {

  $('form').submit(function(event) {
    event.preventDefault();
    
    $('#track-features').empty();
    let artist = $('.form-control').val();
    // alert(country);

    $.get('/track_features?'+$.param({artist: artist}), function(artist_tracks) {

        track = artist_tracks[0]
        features = artist_tracks[0].features
        features.forEach(function(feature){
            let div = $('<div class="sp-entity-container"><a href='+feature.track_href+'>Track Name: '+track.track+'</div>');
            //TODO Include visual analysis for song


           div.appendTo('#track-features');
        // show the track information
    
        });

    	
    });

    // Send a request to our backend (server.py) to get new releases for the currently selected country
    // $.get('/new_releases?' + $.param({country: country}), function(new_releases) {
      
    //   // Loop through each album in the list
    //   new_releases.albums.items.forEach(function(release) {
        
    //     // Use the returned information in the HTML
    //     let div = $('<div class="sp-entity-container"><a href="' + release.external_urls.spotify + 
    //             '"><div style="background:url(\'' + release.images[0].url + 
    //             '\')" class="sp-cover" alt="Album cover"></div></a><h3 class="sp-title">' + release.name + 
    //             '</h3><p class="text-grey-55 sp-by">By ' + release.artists[0].name + '</p></div>')
        
    //     div.appendTo('#new-releases')
        
    //   });
    // });
  });

});
