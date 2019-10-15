import * as React from 'react';
import Enzyme, { shallow } from 'enzyme';
import EnzymeAdapter from 'enzyme-adapter-react-16';
import App from '../App'


Enzyme.configure({ adapter: new EnzymeAdapter() });

describe('App', () => {
  it('renders without crashing', () => {
    const wrapper = shallow(<App />)
    const mockStateOfPlayerName = 'Princess Peach'

    const divTag = wrapper.find('div')
    expect(divTag.length).toEqual(1)
    expect(divTag.find('.cssClassName').length).toEqual(1)

    const h1Tag = wrapper.find('h1')
    expect(h1Tag.length).toEqual(1)
    expect(h1Tag.text()).toEqual(`Hello World ${ mockStateOfPlayerName }!`)

  });
});