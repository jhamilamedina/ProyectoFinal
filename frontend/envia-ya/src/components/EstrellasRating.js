import React, { useState } from 'react';
import './EstrellasRating.css';

const EstrellasRating = ({ rating }) => {
  const [currentRating, setCurrentRating] = useState(rating);
  const [hover, setHover] = useState(null);

  return (
    <div className="star-rating">
      {[...Array(5)].map((star, index) => {
        const ratingValue = index + 1;
        return (
          <label key={index}>
            <input
              type="radio"
              name="rating"
              value={ratingValue}
              onClick={() => setCurrentRating(ratingValue)}
            />
            <svg
              className="star"
              height="25px"
              width="23px"
              viewBox="0 0 25 23"
              fill={ratingValue <= (hover || currentRating) ? "#FFD700" : "#e4e5e9"}
              onMouseEnter={() => setHover(ratingValue)}
              onMouseLeave={() => setHover(null)}
            >
              <polygon strokeWidth="0" points="9.9, 1.1, 12.5, 7.5, 19.1, 7.5, 13.6, 11.6, 15.8, 18.1, 9.9, 14, 4, 18.1, 6.2, 11.6, 0.7, 7.5, 7.3, 7.5" />
            </svg>
          </label>
        );
      })}
    </div>
  );
};

export default EstrellasRating;
