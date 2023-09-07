function set_page_title() {
    document.title = document.getElementById("page_title").innerText

}


function disappear_page() {
    document.body.classList.remove('fade-in');
    document.body.classList.add('fade-out');
}


function appear_page() {
    document.body.classList.remove('fade-out');
    document.body.classList.add('fade-in');
}


function load_page(url) {
    axios(url, {
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    }).then((response) => {
        document.body.innerHTML = response.data;

        set_anchors_click_event_listener()
        set_page_title()
        appear_page()
    }).catch(error => console.error('Ошибка загрузки страницы:', error));
}


function set_anchors_click_event_listener() {
    var anchors = document.querySelectorAll('a')

    anchors.forEach(function(anchor) {
        anchor.addEventListener('click', function(event) {
            event.preventDefault();

            disappear_page()

            setTimeout(function() {
                var href = event.target.getAttribute('href');

                if (!href) {
                    var parent = event.target.parentNode

                    while (true) {
                        if (parent.tagName == "A") {
                            href = parent.getAttribute('href')
                            break
                        } else {
                            parent = parent.parentNode
                        }
                    }
                }

                window.history.pushState({}, "", href);
                load_page(href);
            }, 250);
        });
    });
}


function wait_burger_opening() {
    document.getElementsByClassName("burger-container")[0].classList.toggle("active_burger")
    document.getElementsByClassName("burger")[0].removeEventListener("transitionend", wait_burger_opening)
}


function open_burger() {
    document.getElementsByClassName("hamburger-menu")[0].classList.toggle('active_hamburger');
    document.getElementsByClassName("burger")[0].addEventListener("transitionend", wait_burger_opening)
    document.getElementsByClassName("hamburger-menu")[0].onclick = close_burger
    document.body.style.overflow = 'hidden';
}

function wait_burger_content_closing() {
    document.getElementsByClassName("hamburger-menu")[0].classList.toggle('active_hamburger');
    document.getElementsByClassName("burger-container")[0].removeEventListener("transitionend", wait_burger_content_closing)
}

function close_burger() {
    document.getElementsByClassName("burger-container")[0].classList.toggle("active_burger")
    document.getElementsByClassName("burger-container")[0].addEventListener("transitionend", wait_burger_content_closing)
    document.getElementsByClassName("hamburger-menu")[0].onclick = open_burger
    document.body.style.overflow = 'auto';
}


load_page(window.location.search)
