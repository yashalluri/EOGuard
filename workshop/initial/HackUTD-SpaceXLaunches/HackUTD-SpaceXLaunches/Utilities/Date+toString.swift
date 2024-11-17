//
//  Date+toString.swift
//  HackUTD-SpaceXLaunches
//
//  Created by Nihaal Manesia on 11/11/24.
//

import Foundation

extension Date {
    func toString() -> String {
        let df = DateFormatter()
        df.dateStyle = .long
        return df.string(from: self)
    }
}
