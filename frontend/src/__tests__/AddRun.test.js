import * as React from 'react';
import Enzyme, { shallow } from 'enzyme';
import EnzymeAdapter from 'enzyme-adapter-react-16';
import App from '../App'


Enzyme.configure({ adapter: new EnzymeAdapter() });

describe('AddRun', () => {
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
    wrapper = shallow(<App {...mockProps}/>)
  })
  
  xit('has the athlete\'s user information in props', () => {
    // https://airbnb.io/enzyme/docs/api/ShallowWrapper/props.html
    // const wrapper = shallow(<App user={mockUser} />)
    console.log(wrapper.props())
    expect(wrapper.props().user).toEqual(mockUser)
  })

  xit('displays a form for inputting an Activity', () => {
    const h1Tag = wrapper.find('h1')
    expect(h1Tag.length).toEqual(1)
    expect(h1Tag.text()).toEqual('Add Run')

    const addActivityForm = wrapper.find('form')
    expect(addActivityForm.find('label').length).toEqual(4)

    // expect(addActivityForm.find('label'))[0].text().toEqual('Type:')
    addActivityForm.find('label').forEach((node) => {

      expect(node.text()).toEqual(expect.anything())
    })
  })

  xit('makes a call to the API when clicking the submit button', () => {
    
  })
  xit('gets a response from the API', () => {
    // https://jestjs.io/docs/en/tutorial-async
    // https://jestjs.io/docs/en/asynchronous

  })
})