import React from 'react';
import './Evaluacion.css';

const Reviews = () => {
  return (
    <div className="reviews-container">
      <h2>Comentarios</h2>
      <div className="reviews">
        <div className="review-card">
          <p>“Lorem ipsum dolor sit amet, consectetur adipiscing elit Etiam in tortor eu 
            sapien consequat placerat. 
            Aenean vestibulum erat dictum odio fringilla rutrum.....”</p>
          <div className="review-author">
            <img src="" alt="" />
            <div>
              <p></p>
              <p></p>
            </div>
          </div>
        </div>
        <div className="review-card">
          <p>“Phasellus quis nisi ac tellus sagittis hendrerit ac eget libero.
            Integer ut neque finibus, sodales justo a, placerat nulla.
            Etiam venenatis lacus vitae metus vestibulum, ac bibendum elit venenatis.
            Maecenas imperdiet diam in magna tempor, sit amet porta metus egestas.
            Ut porta nisl ut ipsum auctor facilisis....”</p>
          <div className="review-author">
            <img src="" alt="" />
            <div>
              <p></p>
              <p></p>
            </div>
          </div>
        </div>
      </div>
      
    </div>
  );
}

export default Reviews;
