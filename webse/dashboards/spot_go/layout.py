html_layout = """
    <!DOCTYPE html>
    <html>
        <head>
            {%metas%}
            <title>{%title%}</title>
            {%favicon%}
            {%css%}
            
            <meta charset="UTF-8" />
            <meta http-equiv="X-UA-Compatible" content="IE=edge" />
            <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            
        </head>
        
        <body>
            <!-- Navbar -->
            <header class="site-header">
                  <nav class="navbar navbar-expand-lg navbar-default.navbar-fixed-top navbar-dark py-3", style="background-color:#f2935c;">
                    <div class="container">                  
                      <a href="/" class="navbar-brand", style="font-size: 21px;">Sustainable Energy</a>
                        <button
                          class="navbar-toggler"
                          type="button"
                          data-bs-toggle="collapse"
                          data-bs-target="#navmenu"
                        >
                          <span class="navbar-toggler-icon"></span>
                        </button>
                        <div class="collapse navbar-collapse" id="navbarText_left">                                                           
                            <ul class="navbar-nav mr-auto">
                              <li class="nav-item active">
                                <a class="nav-link", style="font-size: 16px;" href="/register">Register </a>
                              </li>
                              <li class="nav-item">
                                <a class="nav-link", style="font-size: 16px;" href="/login">Login</a>
                              </li>
                            </ul>
                        </div>
                        <div class="collapse navbar-collapse" id="navbarText_right">
                            <ul class="navbar-nav ms-auto">
                              <li class="nav-item active">
                                <a class="nav-link", style="font-size: 16px;" href="/dashboards/home">Dashboards</a>
                              </li>
                              <li class="nav-item active">
                                <a class="nav-link", style="font-size: 16px;" href="/students_apps/home_developers">Students Apps</a>
                              </li>
                              <li class="nav-item">
                                <a class="nav-link", style="font-size: 16px;" href="#">Students Thesis</a>
                              </li>
                              <li class="nav-item">
                                <a class="nav-link", style="font-size: 16px;" href="/app_calculator">App Calculator</a>
                              </li>
                              <li class="nav-item">
                                <a class="nav-link", style="font-size: 16px;" href="/teachers">Teachers</a>
                              </li>
                            </ul>
                        </div>
                    </div>
                  </nav>
                </header>
                <section>
                    <header class="header_css", style="background-color=#f2d95c">
                        <div class="container">
                            <div class="d-sm-flex align-items-center justify-content-between">
                              <div class="col-lg-7 col-md-7 col-sm-6 col-12">
                                <h1><span class="text-warning"> Spot - Guarantees of Origin App</span></h1>
                                <p, style="font-size: 14px;">Consumers, governments and corporations are becoming more aware of the origin of the energy that they consume, 
                                and the guarantees of origin (GO) market is increasing in Europe and worldwide. <strong>More than 25% of the electricity 
                                consumed in Europe is consumed by using GO markets. </strong>
                                </br>
                                </br>
                                We work out the <strong>subgame perfect Nash equilibrium</strong> when the spot and the GO markets operate sequentially, and different market 
                                designs are implemented in the GO market. 
                                </br>
                                </br>
                                We find that the introduction of GO market could have a <strong>pro-competitive effect</strong> in the spot market. 
                                Moreover, the change on prices in the spot market induced by the introduction of a GO market could <strong>reverse the 
                                flow of electricity</strong> between nodes in the spot market.
                                </p>
                                <div class="container_buttons_links_header">
                                   <div class="btn">
                                       <a href="/static/material/dashboards/spot-go/spot_go_may_2022.pdf" class="btn btn-primary btn-lg mr-2", style="background-color=#007bff;">Paper</a>
                                   </div>
                                </div>
                              </div>
                              <div class="col-lg-4 col-md-4 col-sm-5 col-12">                                  
                                  <img src="/static/figures/dashboards/spot-go/spot_go_icon.svg" />
                              </div>
                            </div>
                        </div>
                    </header>
                </section>
            {%app_entry%}
            
                 <section id="developer", style="background-color:#6c757d;">
                    <div class="container">
            
                        <div class="section_developers3_css">
                            <div class="box">
                                <h5 class="card-title mb-3">Arve, Malin</h5>
                                <div class="card-body text-center">
                                    <div class="container_buttons_developers">
                                       <div class="btn">
                                           <a href="https://www.nhh.no/en/employees/faculty/malin-arve/" class="btn btn-primary btn-lg mr-2", style="background-color=#007bff;">Web</a>
                                       </div>
                                    </div>
                                </div>
                            </div>
                            <div class="box">
                                <h5 class="card-title mb-3">Bjørndal, Endre</h5>
                                <div class="card-body text-center">
                                    <div class="container_buttons_developers">
                                       <div class="btn">
                                           <a href="https://www.nhh.no/en/employees/faculty/endre-bjorndal/" class="btn btn-primary btn-lg mr-2", style="background-color=#007bff;">Web</a>
                                       </div>
                                    </div>
                                </div>
                            </div>
                            <div class="box">
                                <h5 class="card-title mb-3">Bjørndal, Mette</h5>
                                <div class="card-body text-center">
                                    <div class="container_buttons_developers">
                                       <div class="btn">
                                           <a href="https://www.nhh.no/en/employees/faculty/mette-helene-bjorndal" class="btn btn-primary btn-lg mr-2", style="background-color=#007bff;">Web</a>
                                       </div>
                                    </div>
                                </div>
                            </div>
                        </div>
            
                        <div class="section_developers2_css">
                            <div class="box">
                                <h5 class="card-title mb-3">Blázquez, Mario</h5>
                                <div class="card-body text-center">
                                    <div class="container_buttons_developers">
                                       <div class="btn">
                                           <a href="https://www.nhh.no/en/employees/faculty/mario-blazquez-de-paz/" class="btn btn-primary btn-lg mr-2", style="background-color=#007bff;">Web</a>
                                       </div>
                                    </div>
                                </div>
                            </div>
                            <div class="box">
                                <h5 class="card-title mb-3">Hovdhal, Isabel</h5>
                                <div class="card-body text-center">
                                    <div class="container_buttons_developers">
                                       <div class="btn">
                                           <a href="https://www.nhh.no/en/employees/faculty/isabel-montero-hovdahl/" class="btn btn-primary btn-lg mr-2", style="background-color=#007bff;">Web</a>
                                       </div>
                                    </div>
                                </div>
                            </div>
                            <div class="box", style="background-color:#6c757d;">
                                
                            </div>
                        </div>
            
                        
                       
            
                    </div>
              </section>
            
            <footer class="p-5  text-white text-center position-relative", style="background-color:#f2935c">
                <div class="container">
                    <p class="lead">ENE425 - Sustainable Energy and App Development</p>
            
                    <a href="#" class="position-absolute bottom-0 end-0 p-5">
                      <i class="bi bi-arrow-up-circle h1"></i>
                    </a>
                  </div>
                {%config%}
                {%scripts%}
                    <script type="text/x-mathjax-config">
                    MathJax.Hub.Config({
                        tex2jax: {
                        inlineMath: [ ['$','$'],],
                        processEscapes: true
                        }
                    });
                    </script>
                {%renderer%}
            </footer>
            <script
              src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.1/dist/js/bootstrap.bundle.min.js"
              integrity="sha384-gtEjrD/SeCtmISkJkNUaaKMoLD0//ElJ19smozuHV6z3Iehds+3Ulb9Bn9Plx0x4"
              crossorigin="anonymous"
            ></script>
            <script src="https://api.mapbox.com/mapbox-gl-js/v2.1.1/mapbox-gl.js"></script>
        
            <script>
              mapboxgl.accessToken =
                'pk.eyJ1IjoiYnRyYXZlcnN5IiwiYSI6ImNrbmh0dXF1NzBtbnMyb3MzcTBpaG10eXcifQ.h5ZyYCglnMdOLAGGiL1Auw'
              var map = new mapboxgl.Map({
                container: 'map',
                style: 'mapbox://styles/mapbox/streets-v11',
                center: [-71.060982, 42.35725],
                zoom: 18,
              })
            </script>
        
            <!-- Optional JavaScript -->
            <!-- jQuery first, then Popper.js, then Bootstrap JS -->
            <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
            <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>

        </body>
    </html>
    """