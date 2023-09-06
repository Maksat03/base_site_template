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
    fetch(url)
        .then(response => response.text())
        .then(data => {
            document.body.innerHTML = data;

            set_anchors_click_event_listener()
            set_page_title()
            appear_page()
        })
        .catch(error => console.error('Ошибка загрузки страницы:', error));
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
            }, 500);
        });
    });
}


set_anchors_click_event_listener()
set_page_title()


function open_burger() {
    document.getElementsByClassName("burger")[0].style.display = "flex"
    document.getElementsByClassName("burger")[0].style.height = "100%"
    document.getElementsByClassName("hamburger-menu")[0].classList.toggle('active_hamburger');
    document.getElementsByClassName("hamburger-menu")[0].onclick = close_burger
}


function close_burger() {
    document.getElementsByClassName("burger")[0].style.display = "none"
    document.getElementsByClassName("burger")[0].style.height = "0px"
    document.getElementsByClassName("hamburger-menu")[0].classList.toggle('active_hamburger');
    document.getElementsByClassName("hamburger-menu")[0].onclick = open_burger
}
