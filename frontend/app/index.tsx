import Clickable from '@/components/Clickable';

const FlatListBasics = () => {
  return (
    <>
      <Clickable title="Press Me" onPress={() => alert('Button pressed!')}/>
      <Clickable title="Press Me" onPress={() => alert('Button pressed!')}/>
      <Clickable title="Press Me" onPress={() => alert('Button pressed!')}/>
      <Clickable title="Press Me" onPress={() => alert('Button pressed!')}/>
    </>

  );
};

export default FlatListBasics;