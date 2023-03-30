import axios from 'axios'
import { VUE_APP_API_URL } from './config'

export const fetchautos = () => {
  // let url = `http://127.0.0.1:5000/api/v1/autos`
  let url = `${ VUE_APP_API_URL}/api/v1/autos`

  return axios.get(url)
  .then(response => {
    return response.data
  })
}

export const createAuto = (params) => {
  let url = `${ VUE_APP_API_URL }/api/v1/autos`

  return axios.post(url, {
    brand: params.brand,
    model: params.model,
    year: params.year
  }, {
    "Content-Type": "application/json"
  })
    .then(resp => resp)
}

