import type {CategoricalMapper} from "./categorical_mapper"
import {cat_v_compute} from "./categorical_mapper"
import {ColorMapper} from "./color_mapper"
import type {Factor} from "../ranges/factor_range"
import {FactorSeq} from "../ranges/factor_range"

import type * as p from "core/properties"
import type {Arrayable, ArrayableOf} from "core/types"

export namespace CategoricalColorMapper {
  export type Attrs = p.AttrsOf<Props>

  export type Props = ColorMapper.Props & CategoricalMapper.Props
}

export interface CategoricalColorMapper extends CategoricalColorMapper.Attrs {}

export class CategoricalColorMapper extends ColorMapper {
  declare properties: CategoricalColorMapper.Props

  constructor(attrs?: Partial<CategoricalColorMapper.Attrs>) {
    super(attrs)
  }

  static {
    this.define<CategoricalColorMapper.Props>(({Number, Nullable}) => ({
      factors: [ FactorSeq ],
      start:   [ Number, 0 ],
      end:     [ Nullable(Number), null ],
    }))
  }

  protected _v_compute<T>(data: ArrayableOf<Factor>, values: Arrayable<T>,
      palette: Arrayable<T>, {nan_color}: {nan_color: T}): void {
    cat_v_compute(data, this.factors, palette, values, this.start, this.end, nan_color)
  }
}
