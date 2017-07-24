$(document).ready(function(){

        // To make nav-bar responsive
        $('#nav-icon').click(function(){
          $(this).toggleClass('open');
          var x = document.getElementById("main-sidenav");
          if(x.className === "sidenav"){
              x.className += " responsive";
          }else{
              x.className = "sidenav";
          }
        });

        // to kick in animation
        new WOW().init();

        // for smooth scrolling of nav bar links
      $('a[href*="#"]')
        // Remove links that don't actually link to anything
        .not('[href="#"]')
        .not('[href="#0"]')
        .click(function(event) {
          // On-page links
          if (
            location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') 
            && 
            location.hostname == this.hostname
          ) {
            // Figure out element to scroll to
            var target = $(this.hash);
            target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
            // Does a scroll target exist?
            if (target.length) {
              // Only prevent default if animation is actually gonna happen
              event.preventDefault();
              $('html, body').animate({
                scrollTop: target.offset().top
              }, 1000, function() {
                // Callback after animation
                // Must change focus!
                var $target = $(target);
                $target.focus();
                if ($target.is(":focus")) { // Checking if the target was focused
                  return false;
                } else {
                  $target.attr('tabindex','-1'); // Adding tabindex for elements not focusable
                  $target.focus(); // Set focus again
                };
              });
            }
          }
        });

        // to add and remove active class
        var selector = '#main-sidenav li';
        $(selector).removeClass('active');
        $(selector).on('click', function(){
            $(selector).removeClass('active');
            $(this).addClass('active');
        });


        //UP ARROW JS
                  // ===== Scroll to Top ==== 
        $(window).scroll(function() {
            if ($(this).scrollTop() >= 50) {        // If page is scrolled more than 50px
                $('#return-to-top').fadeIn(200);    // Fade in the arrow
            } else {
                $('#return-to-top').fadeOut(200);   // Else fade out the arrow
            }
        });
        $('#return-to-top').click(function() {      // When arrow is clicked
            $('body,html').animate({
                scrollTop : 0                       // Scroll to top of body
            }, 500);
        });


      $('#fullpage').fullpage({
          //Navigation
          menu: '#menu',
          lockAnchors: false,
          navigation: false,
          navigationPosition: 'right',
          navigationTooltips: ['firstSlide', 'secondSlide'],
          showActiveTooltip: false,
          slidesNavigation: false,
          slidesNavPosition: 'bottom',

          //Scrolling
          css3: false,
          scrollingSpeed: 800,
          autoScrolling: true,
          fitToSection: true,
          fitToSectionDelay: 3000,
          scrollBar: true,
          easing: 'easeInOutCirc',
          easingcss3: 'ease',
          loopBottom: false,
          loopTop: false,
          loopHorizontal: true,
          continuousVertical: false,
          continuousHorizontal: false,
          scrollHorizontally: false,
          interlockedSlides: false,
          dragAndMove: false,
          offsetSections: false,
          resetSliders: false,
          fadingEffect: false,
          normalScrollElements: '#element1, .element2',
          scrollOverflow: false,
          scrollOverflowReset: true,
          scrollOverflowOptions: null,
          touchSensitivity: 15,
          normalScrollElementTouchThreshold: 5,
          bigSectionsDestination: null,

          //Accessibility
          keyboardScrolling: true,
          animateAnchor: true,
          recordHistory: true,

          //Design
          controlArrows: true,
          verticalCentered: false,
          // sectionsColor : ['#ccc', '#fff'],
          paddingTop: '0em',
          paddingBottom: '0px',
          fixedElements: '#header,',
          responsiveWidth: 768,
          responsiveHeight: 0,
          responsiveSlides: false,
          parallax: false,
          parallaxOptions: {type: 'reveal', percentage: 100, property: 'translate'},

          //Custom selectors
          sectionSelector: '.section',
          slideSelector: '.slide',

          lazyLoading: true,

          //events
          onLeave: function(index, nextIndex, direction){},
          afterLoad: function(anchorLink, index){},
          afterRender: function(){},
          afterResize: function(){},
          afterResponsive: function(isResponsive){},
          afterSlideLoad: function(anchorLink, index, slideAnchor, slideIndex){},
          onSlideLeave: function(anchorLink, index, slideIndex, direction, nextSlideIndex){}
        });




});