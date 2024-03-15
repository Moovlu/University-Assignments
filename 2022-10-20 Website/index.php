<?php
    $pageName = 'Home';
    require_once("tools.php");
    require_once("segments/head.php");
?>
            <nav>
                <div id="navbar">
                    <a href=#about>About Us</a>
                    <a href=#whoWeAre>Who We Are</a>
                    <a href=#service>Service Area</a>
                    <a href="booking.php">Book an Appointment</a>
                    <a href='administration.php'>Admin page</a>
                </div>
            </nav>
        </div>

        <main>
            <!-- JQuery Carousel -->
            <div class="slider center">
                <div><img src="resources/carousel1.jpg" alt="reception desk"></div>
                <div><img src="resources/carousel2.jpg" alt="hand holding"></div>
                <div><img src="resources/carousel3.jpg" alt="hands making love heart"></div>
                <div><img src="resources/carousel4.jpg" alt="surgeon giving thumbs up"></div>
                <div><img src="resources/carousel5.jpg" alt="hand holding"></div>
            </div>

            <article>
                <div id="about">
                    <h2>About Us</h2>
                    <div class="center">
                        Russel Street Medical opened in 2020 and is located in Melbourne's CBD at 340 Russel Street Melbourne, just opposite The Old Melbourne Jail and within walking distance of Melbourne Central Train Station.
                        We strive to help all of our patients with a focus on preventative health care, a view to managing chronic health conditions with a holistic approach, and with access to a wide range of specialist care providers when needed.
                        Under partnerships, we are able to offer RMIT students & staff discounted rates.<br><br>
                        <b>Opening Times</b><br>
                        Monday - Sunday<br>
                        9am - 6pm
                    </div>
                </div>

                <table class="center">
                    <tr>
                        <th>Consultation</th>
                        <th>Normal Fee</th>
                        <th>RMIT Member Fee</th>
                        <th>Medicare Fee</th>
                    </tr>
                    <tr>
                        <td>Standard</td>
                        <td>$85.00</td>
                        <td>$60.50</td>
                        <td>$39.75</td>
                    </tr>
                    <tr>
                        <td>Long or Complex</td>
                        <td>$130.00</td>
                        <td>$91.00</td>
                        <td>$76.95</td>
                    </tr>
                </table>
            </article>

            <section>
                <h2 id="whoWeAre">Who We Are</h2>
                <div class="whoContainer">
                    <div>
                        <img src="resources/abigale.jpg" alt="abigale">
                        <h3>Dr. Abigale Laurentis</h3>
                        <p>
                            Abigale Laurentis completed her medical degree at the University of Queensland in 2013, where she also obtained a Bachelor of Science in Biomedicine.<br>
                            Over her training and practice, Abigale has worked in a variety of clinical settings including specialities at Latrobe Health.
                        </p>
                    </div>
                    <div>
                        <img src="resources/stephen.jpg" alt="stephen">
                        <h3>Dr. Stephen Hill</h3>
                        <p>
                            Stephen Hill graduated from Auckland University in New Zealand in 2014, and obtained his Fellowship from the Royal Australian College of General Practitioners in 2017.<br>
                            Over his training and practice, Stephen worked in internal medicine at the Royal Children's Hospital Melbourne before transitioning to General Practice.
                        </p>
                    </div>
                    <div>
                        <img src="resources/kiyoko.jpg" alt="kiyoko">
                        <h3>Ms Kiyoko Tsu</h3>
                        <p>
                            Kiyoko Tsu completed her Bachelor of Nursing at the Yong Loo Lin School of Medicine in Singapore in 2019.<br>
                            She is an accredited Nurse Immuniser and has worked in various hospitals within metropolitan Melbourne.
                        </p>
                    </div>
                </div>
            </section>
            
            <section>
                <h2 id="service">Service Area</h2>
                <div class="serviceContainer">
                    <div>
                        <h3>Are you new to our clinic?</h3>
                        <p>Drop in during our opening hours to register with us in person.</p>
                    </div>
                    <div>
                        <h3>Already have an account?</h3>
                        <p>Use the <a href="booking.php">online booking system</a> to book vaccination and blood tests</p>
                    </div>
                </div>
            </section>

        </main>
<?php require_once("segments/footer.php"); ?>