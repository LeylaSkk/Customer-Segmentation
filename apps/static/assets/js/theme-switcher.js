$(document).ready(function () {
    let light_color = localStorage.getItem("light_color");

    if (light_color === "true") {
        $('body').addClass('white-content');
        $('.switch input').prop("checked", false);
    } else {
        $('.switch input').prop("checked", true);
    }

    $('.switch input').on("change", function () {
        light_color = localStorage.getItem("light_color");

        if (light_color === "true") {
            localStorage.setItem("light_color", "false");

            $('body').addClass('change-background');
            setTimeout(function () {
                $('body').removeClass('change-background');
                $('body').removeClass('white-content');
            }, 400);

        } else {
            localStorage.setItem("light_color", "true");

            $('body').addClass('change-background');
            setTimeout(function () {
                $('body').removeClass('change-background');
                $('body').addClass('white-content');
            }, 400);
        }
    });

    $('.light-badge').click(function () {
        $('body').addClass('white-content');
        localStorage.setItem("light_color", "true");
        $('.switch input').prop("checked", false);
    });

    $('.dark-badge').click(function () {
        $('body').removeClass('white-content');
        localStorage.setItem("light_color", "false");
        $('.switch input').prop("checked", true);
    });
});
