document.addEventListener(
    "DOMContentLoaded",
    function () {


        // =====================================================
        // MENÚ MÓVIL
        // =====================================================

        const navToggle =
            document.getElementById(
                "navToggle"
            );

        const navLinks =
            document.getElementById(
                "navLinks"
            );


        if (
            navToggle &&
            navLinks
        ) {

            navToggle.addEventListener(
                "click",
                function () {

                    navLinks.classList.toggle(
                        "show"
                    );

                }
            );

        }



        // =====================================================
        // PERFIL
        // =====================================================

        const profileToggle =
            document.querySelector(
                "[data-profile-toggle]"
            );

        const profileMenu =
            document.querySelector(
                "[data-profile-menu]"
            );


        if (
            profileToggle &&
            profileMenu
        ) {

            profileToggle.addEventListener(
                "click",
                function (event) {

                    event.stopPropagation();

                    profileMenu.classList.toggle(
                        "show"
                    );

                }
            );


            document.addEventListener(
                "click",
                function () {

                    profileMenu.classList.remove(
                        "show"
                    );

                }
            );


            profileMenu.addEventListener(
                "click",
                function (event) {

                    event.stopPropagation();

                }
            );

        }



        // =====================================================
        // CONTRASEÑAS
        // =====================================================

        document
            .querySelectorAll(
                "[data-password-toggle]"
            )
            .forEach(
                function (button) {

                    button.addEventListener(
                        "click",
                        function () {

                            const inputId =
                                button.dataset
                                    .passwordToggle;

                            const input =
                                document.getElementById(
                                    inputId
                                );


                            if (!input) {

                                return;

                            }


                            if (
                                input.type ===
                                "password"
                            ) {

                                input.type =
                                    "text";

                            } else {

                                input.type =
                                    "password";

                            }

                        }
                    );

                }
            );



        // =====================================================
        // MODALES
        // =====================================================

        document
            .querySelectorAll(
                "[data-modal-open]"
            )
            .forEach(
                function (button) {

                    button.addEventListener(
                        "click",
                        function () {

                            const id =
                                button.dataset
                                    .modalOpen;

                            const modal =
                                document.getElementById(
                                    id
                                );


                            if (modal) {

                                modal.classList.add(
                                    "show"
                                );

                                document.body.classList.add(
                                    "modal-open"
                                );

                            }

                        }
                    );

                }
            );


        function closeModal(
            modal
        ) {

            modal.classList.remove(
                "show"
            );

            document.body.classList.remove(
                "modal-open"
            );

        }


        document
            .querySelectorAll(
                "[data-modal-close]"
            )
            .forEach(
                function (button) {

                    button.addEventListener(
                        "click",
                        function () {

                            const modal =
                                button.closest(
                                    ".modal"
                                );

                            if (modal) {

                                closeModal(
                                    modal
                                );

                            }

                        }
                    );

                }
            );


        document
            .querySelectorAll(
                ".modal"
            )
            .forEach(
                function (modal) {

                    modal.addEventListener(
                        "click",
                        function (event) {

                            if (
                                event.target ===
                                modal
                            ) {

                                closeModal(
                                    modal
                                );

                            }

                        }
                    );

                }
            );


        document.addEventListener(
            "keydown",
            function (event) {

                if (
                    event.key ===
                    "Escape"
                ) {

                    document
                        .querySelectorAll(
                            ".modal.show"
                        )
                        .forEach(
                            closeModal
                        );

                }

            }
        );



        // =====================================================
        // CONFIRMACIONES
        // =====================================================

        document
            .querySelectorAll(
                "form[data-confirm]"
            )
            .forEach(
                function (form) {

                    form.addEventListener(
                        "submit",
                        function (event) {

                            const message =
                                form.dataset
                                    .confirm;

                            const confirmed =
                                window.confirm(
                                    message
                                );


                            if (
                                !confirmed
                            ) {

                                event.preventDefault();

                            }

                        }
                    );

                }
            );



        // =====================================================
        // BUSCADOR DE EVENTOS
        // =====================================================

        const eventSearch =
            document.getElementById(
                "eventSearch"
            );

        const eventTypeFilter =
            document.getElementById(
                "eventTypeFilter"
            );


        function filterEvents() {

            const cards =
                document.querySelectorAll(
                    "[data-event-card]"
                );


            if (
                cards.length === 0
            ) {

                return;

            }


            const search =
                eventSearch
                    ? eventSearch.value
                        .toLowerCase()
                    : "";


            const type =
                eventTypeFilter
                    ? eventTypeFilter.value
                    : "all";


            let visible = 0;


            cards.forEach(
                function (card) {

                    const text =
                        (
                            card.dataset.search ||
                            ""
                        ).toLowerCase();


                    const cardType =
                        card.dataset.type;


                    const matchesSearch =
                        text.includes(
                            search
                        );


                    const matchesType =
                        type ===
                            "all" ||
                        cardType ===
                            type;


                    const show =
                        matchesSearch &&
                        matchesType;


                    card.style.display =
                        show
                            ? ""
                            : "none";


                    if (show) {

                        visible++;

                    }

                }
            );


            const empty =
                document.getElementById(
                    "eventFilterEmpty"
                );


            if (empty) {

                empty.classList.toggle(
                    "hidden",
                    visible !== 0
                );

            }

        }


        if (
            eventSearch
        ) {

            eventSearch.addEventListener(
                "input",
                filterEvents
            );

        }


        if (
            eventTypeFilter
        ) {

            eventTypeFilter.addEventListener(
                "change",
                filterEvents
            );

        }



        // =====================================================
        // VENTAS
        // =====================================================

        const saleSearch =
            document.getElementById(
                "saleSearch"
            );


        let activeSaleStatus =
            "all";


        function filterSales() {

            const cards =
                document.querySelectorAll(
                    "[data-sale-card]"
                );


            if (
                cards.length === 0
            ) {

                return;

            }


            const search =
                saleSearch
                    ? saleSearch.value
                        .toLowerCase()
                    : "";


            let visible = 0;


            cards.forEach(
                function (card) {

                    const text =
                        (
                            card.dataset.search ||
                            ""
                        ).toLowerCase();


                    const status =
                        card.dataset.status;


                    const matchesSearch =
                        text.includes(
                            search
                        );


                    const matchesStatus =
                        activeSaleStatus ===
                            "all" ||
                        activeSaleStatus ===
                            status;


                    const show =
                        matchesSearch &&
                        matchesStatus;


                    card.style.display =
                        show
                            ? ""
                            : "none";


                    if (show) {

                        visible++;

                    }

                }
            );


            const empty =
                document.getElementById(
                    "saleFilterEmpty"
                );


            if (empty) {

                empty.classList.toggle(
                    "hidden",
                    visible !== 0
                );

            }

        }


        if (
            saleSearch
        ) {

            saleSearch.addEventListener(
                "input",
                filterSales
            );

        }


        document
            .querySelectorAll(
                "[data-sale-status]"
            )
            .forEach(
                function (button) {

                    button.addEventListener(
                        "click",
                        function () {

                            document
                                .querySelectorAll(
                                    "[data-sale-status]"
                                )
                                .forEach(
                                    function (
                                        element
                                    ) {

                                        element
                                            .classList
                                            .remove(
                                                "active"
                                            );

                                    }
                                );


                            button.classList.add(
                                "active"
                            );


                            activeSaleStatus =
                                button.dataset
                                    .saleStatus;


                            filterSales();

                        }
                    );

                }
            );



        // =====================================================
        // TOASTS
        // =====================================================

        setTimeout(
            function () {

                document
                    .querySelectorAll(
                        ".toast"
                    )
                    .forEach(
                        function (toast) {

                            toast.classList.add(
                                "toast-hide"
                            );


                            setTimeout(
                                function () {

                                    toast.remove();

                                },
                                300
                            );

                        }
                    );

            },
            3500
        );



        // =====================================================
        // ICONOS
        // =====================================================

        if (
            window.lucide
        ) {

            lucide.createIcons();

        }


    }
);