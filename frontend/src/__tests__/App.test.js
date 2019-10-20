import * as React from 'react';
import Enzyme, { shallow, mount } from 'enzyme';
import EnzymeAdapter from 'enzyme-adapter-react-16';
import App from '../App'
import AddRun from '../AddRun';


Enzyme.configure({ adapter: new EnzymeAdapter() });

describe('App', () => {
  let wrapper
  const mockUser = {
    id: 127,
    name: 'Michael Jordan',
    athlete_id: 25
  }
  const mockProps = {
    user: mockUser
  }
  beforeEach(() => {
    wrapper = mount(<App {...mockProps}/>)
  })

  it('initialises with the AddRun function component', () => {
    const firstChildInDiv = wrapper.children().childAt(0)
    const addRunComponent = wrapper.find(AddRun)

    expect(wrapper.props()).toEqual(mockProps)
    expect(firstChildInDiv.length).toEqual(1)
    expect(addRunComponent.length).toEqual(1)
    expect(firstChildInDiv).toMatchObject(addRunComponent)
  })

  it('switches from AddRun to AthleteLog components', () => {
    // const temp = App.changePage('AthleteRunLog')
    expect(wrapper.state('activePage')).toEqual('AthleteRunLog')
    const firstChildInDiv = wrapper.children().childAt(0)
    
    console.log({firstChildInDiv})
    expect(firstChildInDiv.length).toEqual(1)
  })
  
})