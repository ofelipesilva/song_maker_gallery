import React, { Component } from "react";
import "./App.css";
import {
  BrowserRouter as Router,
  Route,
  Switch,
  Redirect,
} from "react-router-dom";

import { Provider } from "react-redux";
import store from "../store";

import LandingPage from "./landing_page/landing_page";
import PrivateRoute from "./generics/private_route";
import SignUp from "./signup-login/signup";
import Login from "./signup-login/login";
import Gallery from "./gallery/gallery";
import Teacher from "./teacher/teacher";
import { Footer } from "./generics/footer";
import { TosPage, PrivacyPage } from "./legal";

class App extends Component {
  render() {
    return (
      <Provider store={store}>
        <Router>
          {/* adsense
          <script
            data-ad-client="ca-pub-2027864288539638"
            async
            src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"
          ></script> */}
          <Switch>
            <Route exact path="/">
              <LandingPage />
            </Route>
            <Route path="/signup">
              <SignUp title="Sign Up" />
              <Footer />
            </Route>
            <Route path="/login">
              <Login title="Login" />
              <Footer />
            </Route>
            <Route path="/gallery/*">
              <Gallery />
            </Route>
            <Route path="/privacy/*">
              <PrivacyPage />
            </Route>
            <Route path="/tos/*">
              <TosPage />
            </Route>
            <PrivateRoute path="/teacher">
              <Teacher title="Gallery Management Console" />
              <Footer />
            </PrivateRoute>
          </Switch>
        </Router>
      </Provider>
    );
  }
}

export default App;
