import React, { Fragment, Component } from "react";

import GalleryBody from "./gal_body";

import { getGallery } from "../../actions/galleries";
import { connect } from "react-redux";

class gallery extends Component {
  state = {
    url_ext: window.location.pathname.split("/")[2],
    gallery: null,
  };

  componentDidMount() {
    console.log("ran");
    this.props.getGallery(this.state.url_ext);
  }

  render() {
    if (this.props.gallery === undefined) {
      console.log("yes");
    }
    console.log("this", this.props);
    return (
      <div>
        {this.props.gallery === undefined ? (
          <h1>Loading</h1>
        ) : (
          <GalleryBody
            title={this.props.gallery.title}
            description={this.props.gallery.description}
            data={this.props.gallery.api_obj}
          />
        )}
      </div>
    );
  }
}

function mapStateToProps(state) {
  const gallery = state.galleries.galleries[0]; // TODO change store state so that there is only one gallery within the gallery sub-state at a time
  return {
    gallery: gallery,
  };
}

export default connect(mapStateToProps, { getGallery })(gallery);
