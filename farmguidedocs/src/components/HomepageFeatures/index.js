import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

const FeatureList = [
  {
    title: 'Informative',
    Svg: require('@site/static/img/farmppl.svg').default,
    description: (
      <>
        Learn about the best practices you could apply in the farm.
      </>
    ),
  },
  {
    title: 'Smart Farming Tips',
    Svg: require('@site/static/img/farmboy.svg').default,
    description: (
      <>
        Get insights to the best practices you could apply on the farm to boost yield.
      </>
    ),
  },
  {
    title: 'Improve productivity',
    Svg: require('@site/static/img/farmgirl.svg').default,
    description: (
      <>
        Improve productivity on the farm today with this guide and make substantial gains.
      </>
    ),
  },
];

function Feature({Svg, title, description}) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
